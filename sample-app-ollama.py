from ollama import Client
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

client = Client(
  os.environ['BASE_URL']
)

deployment=os.environ['CHAT_COMPLETION_MODEL']

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat(model=deployment, messages=messages, options={
    "temperature": 0.1
})


# print response
print("Recipes:")
print(completion.message.content)

old_prompt_result = completion.message.content
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat(model=deployment, messages=messages, options={
    "temperature": 0
})

# print response
print("\n=====Shopping list ======= \n")
print(completion.message.content)