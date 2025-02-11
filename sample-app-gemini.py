from google import genai
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
deployment=os.environ['GEMINI_MODEL']

no_recipes = input("No of recipes (for example, 5: ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}: "

completion = client.models.generate_content(model=deployment, contents=prompt)

# print response
print("Recipes:")
print(completion.text)

old_prompt_result = completion.text
prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "

new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
completion = client.models.generate_content(model=deployment, contents=new_prompt)

# print response
print("\n=====Shopping list ======= \n")
print(completion.text)