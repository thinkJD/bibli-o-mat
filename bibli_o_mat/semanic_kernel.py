import semantic_kernel as sk
from semantic_kernel.ai.open_ai import OpenAITextCompletion


class SemanticKernel:
    def __init__(self, api_key: str, org_id: str):
        self.kernel = sk.Kernel()
        self.kernel.config.add_text_backend(
            "dv", OpenAITextCompletion(
                "text-davinci-003", api_key, org_id))

        book_list_short_story_prompt = """
        1. Use the following list of german book titles to create a short story based on them.
        2. Be curious, friendly and creative
        3. Use 80 words maximum.
        4. Answer in German language.

        ### Book titles
        {{$input}}
        """
        self.book_list_short_story = self.kernel.create_semantic_function(
            book_list_short_story_prompt, max_tokens=2000, temperature=0.2, top_p=0.5)

    def get_short_story(self, book_list):
        return self.book_list_short_story(book_list)
