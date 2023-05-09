# it's a class name PostGenerator using gpt-3 and dalle2 to generate post and photo with title and outline
import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class PostGenerator:
    def __init__(self, engine='gpt-3.5-turbo', title='test title', outline='test outline'):
        self.engine = engine
        self.title = title
        self.outline = outline

    def set_title(self, title):
        self.title = title
    
    def set_outline(self, outline):
        self.outline = outline

    def generate_post(self, prompt='test prompt'):
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[
                # system messages describe the behavior of the AI assistant. A useful system message for data science use cases is "You are a helpful assistant who understands data science."
                # user messages describe what you want the AI assistant to say. We'll cover examples of user messages throughout this tutorial
                # assistant messages describe previous responses in the conversation. We'll cover how to have an interactive conversation in later tasks
                    {"role": "system", "content": os.getenv("SYSTEM_CONTENT")},
                    {"role": "user", "content": prompt},
            ])
        return response["choices"][-1]["message"]["content"]
    
    def generate_photo(self, prompt='test prompt'):
        # this function generate photo from dalle2
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
        )
        return response["data"][0]["url"]

    def generate(self):
        # this function generate post and photo
        post_prompt = f"根據標題 {self.title} 和想要傳達的內容 {self.outline} 生成文章"
        post = self.generate_post(post_prompt)

        photo_prompt = f"根據標題 {self.title} 、想要傳達的內容 {self.outline} 和內容 {post} 生成以風景為主的圖片"
        photo = self.generate_photo(photo_prompt)
        return (post, photo)

if __name__ == "__main__":
    pg = PostGenerator()
    title = "花是生活的必需品，不論男女老少都喜歡"
    outline = "韓國明星以花美男著稱，在宣傳照中經常會使用到花的元素，且他們都喜歡花，請選擇一種花卉，並闡述花的好處以及花語"
    pg.set_title(title)
    pg.set_outline(outline)

    test = pg.generate()
    print(test[0])
    print(test[1])
    
    # post_prompt = f"根據標題 {title} 和想要傳達的內容 {outline} 生成文章"
    # post = pg.generate_post(post_prompt)
    # print(post)


