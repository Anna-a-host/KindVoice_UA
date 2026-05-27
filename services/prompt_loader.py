def load_prompt(mode, lang):

    with open("prompts/base.txt", "r", encoding="utf-8") as file:
        base_prompt = file.read()

    with open(f"prompts/{mode}.txt", "r", encoding="utf-8") as file:
        mode_prompt = file.read()

    with open("prompts/style.txt", "r", encoding="utf-8") as file:
        style_prompt = file.read()

    language_prompt = ("\nRespond ONLY in Ukrainian." if lang == "uk" else "\nRespond ONLY in English.")

    return (base_prompt + style_prompt + "\n" + mode_prompt + language_prompt)