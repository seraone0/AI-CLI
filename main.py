import subprocess
import sys
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key: print("OPENROUTER_API_KEY absent"); sys.exit(1)

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


current_os = sys.platform

print("Enter command: ")

while True:
    request = input()

    if request.lower() in ['exit', 'quit', 'выход']: break
    if not request.strip(): continue

    try: #!
        response = client.chat.completions.create( #!
            model='cohere/north-mini-code:free', #!
            messages=[ #!
                {
                    "role": "system",
                    "content": (
                        f"иты эксперт по системному администрированию твоя задача переводить текстовые запросы пользователя"
                        f"в реальные терминальные команды для операционной системы {current_os}"
                        f"критическое правил возвращай только готовую команду никакого лишнего текста объяснений"
                        f"вводных слов или оформления в блоки кода markdown не используй ```"
                    )
                },
                {"role": "user", "content": request} #!
            ],
            temperature=0.0 #!
        )

        command = response.choices[0].message.content.strip() #!
        print(f"gen {command}")

        confirm = input(f"confirm this command? [Y/n]: ").strip().lower()
        if confirm not in ['', 'y', 'yes', 'д', 'да']:
            print("cancel"); continue

        result = subprocess.run(command, shell=True, text=True, capture_output=True)

        if result.returncode == 0: print(result.stdout)
        else: print(result.stderr)

    except Exception as e: print(f"Error: {e}")