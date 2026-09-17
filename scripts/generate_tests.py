import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_BASE_URL = os.getenv(
    "NVIDIA_BASE_URL",
    "https://integrate.api.nvidia.com/v1",
)
NVIDIA_MODEL = os.getenv(
    "NVIDIA_MODEL",
    "meta/llama-3.2-11b-vision-instruct",
)

client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=NVIDIA_API_KEY,
)


def generate_test_cases(feature: str, format: str = "gherkin", app_type: str = "api"):
    if not NVIDIA_API_KEY:
        raise SystemExit(
            "NVIDIA_API_KEY is not set. Add it to your .env file "
            "(see .env.example)."
        )

    prompt = f"""You are an expert QA Engineer.
Generate comprehensive test cases for: {feature}
Format: {format}
App type: {app_type}

Cover:
1. Happy path
2. Negative cases
3. Edge cases
4. Boundary conditions

Return only test cases, no explanation."""

    completion = client.chat.completions.create(
        model=NVIDIA_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.2,
    )

    content = completion.choices[0].message.content
    if not content:
        raise RuntimeError("NVIDIA API returned an empty response.")
    return content


def save_test_cases(feature: str, content: str):
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    filename = feature.lower().replace(" ", "_")
    filepath = docs_dir / f"{filename}_test_cases.md"

    filepath.write_text(f"# Test Cases: {feature}\n\n{content}", encoding="utf-8")
    print(f"✅ Saved to {filepath}")
    return str(filepath)


if __name__ == "__main__":
    feature = input("Feature name (e.g. Login, Registration): ")
    format = input("Format (gherkin/plain): ") or "gherkin"
    app_type = input("App type (api/mobile/web): ") or "api"

    print(f"\n🤖 Generating test cases for: {feature}...\n")
    try:
        result = generate_test_cases(feature, format, app_type)
    except Exception as exc:
        raise SystemExit(f"❌ Generation failed: {exc}") from exc

    print(result)

    save = input("\n💾 Save to file? (y/n): ")
    if save.lower() == "y":
        save_test_cases(feature, result)
