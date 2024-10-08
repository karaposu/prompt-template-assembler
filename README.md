
# Prompt Template Assembler

**Prompt Template Assembler** is a Python library designed to streamline the creation and management of dynamic prompt templates for AI models.

Instead of handling the entire lifecycle of a prompt, **Prompt Template Assembler** specializes in the **stacking of prompt templates**—unformatted prompts with placeholders—leaving the task of filling in these templates to common LLM libraries like Langchain. This approach can be seen as a **replacement for prompt chaining** in libraries such as LangChain, offering more flexibility and control.

## Key Features

- **Conditional Prompt Stacking**: Stack prompt templates conditionally, allowing the creation of adaptable prompts based on specific scenarios or use cases.
- **Custom Categories for Templates**: Organize prompt templates into user-defined categories, making it easy to call and merge templates based on modular, structured designs.
- **"Send to Bin" Logic**: (Optional) you can temporarily store parts of a prompt in a "bin" and retrieve or merge them at a later point, enabling more dynamic and flexible prompt building over multiple stages.
- **Statement vs. Question Formatting**:  prompts can be defined in a way which allows them to be formatted as informative statements or questions, allowing you to switch between different styles of interactions without changing the core context.
- **Intuitive Interface**: Designed with simplicity and usability in mind, the library enables users to construct prompts effortlessly without complex chaining or dependencies.

## Why Choose Prompt Assembler?

**Prompt Assembler** was built to dynamically **stack and assemble prompts** while sidestepping the inflexible chain structures found in many other libraries. Developers gain fine-grained control over how prompts are built and combined, making it an ideal solution for projects ranging from simple chatbots to complex AI workflows.

The library also includes a **YAML-based prompt management system**, allowing you to store, version, and manage prompts in a human-readable format. This is especially useful for teams working on large-scale AI applications where prompt updates and variations are frequent.

## Error Handling

Prompt Assembler offers robust error handling, ensuring that missing or incorrect placeholders are managed gracefully. The library detects errors early, providing a smooth and reliable prompt generation experience even in production environments.

---

With **Prompt Assembler**, you can simplify and enhance your prompt engineering workflows, whether you're building conversational agents, fine-tuning machine learning models, or managing large-scale AI-driven applications.




It looks like you've put a lot of thought into your `PromptTemplateAssembler` class, making it a powerful tool for dynamic prompt creation and management! To further enhance your documentation, I'll add a usage guide that includes installation steps and a simple example to help users get started. Here’s how you might present it:

---

# How to Use Prompt Template Assembler

## Installation

To get started with **Prompt Template Assembler**, you can install it using pip:

```bash
pip install prompt-template-assembler
```

## Basic Usage

1. **Prepare Your YAML File**: Define your prompt templates in a YAML file (e.g., `prompts.yaml`). Each prompt should have a name, category, and content with placeholders for dynamic insertion:

    ```yaml
    context_prompts:
      - name: business_documentation
        statement_suffix: "Please refer to the following business details."
        info: "Business documentation is crucial for understanding the context of operations."

      - name: user_input
        statement_suffix: "We received the following input from the user."
        info: "User input allows us to tailor our approach based on specific queries."
    
    meta_prompts:
      - name: answer_style
        statement_suffix: "Ensure the answer follows a professional tone."
        info: "The response should maintain a formal and clear language."
    ```

2. **Create a `PromptTemplateAssembler` Object**:

    ```python
    from proteas import PromptTemplateAssembler

    ptos = PromptTemplateAssembler('prompts.yaml')
    ```

3. **Craft Your Prompt**: Define the order of the prompt units you want to include in your template and provide any necessary context data for placeholders:

    ```python
    order = ["business_documentation", "user_input", "answer_style"]
    filtered_data = {
        "business_documentation": "Our company specializes in AI solutions for data analytics.",
        "user_input": "How can I integrate your tool into my current workflow?",
    }

    # Create a crafted prompt template
    prompt_template_1 = ptos.craft(order)
    print(prompt_template_1)
    ```

4. **Format with LangChain** (Optional): Use LangChain to handle any remaining placeholders or further customize the output:

    ```python
    from langchain.prompts import PromptTemplate

    prompt = PromptTemplate.from_template(prompt_template_1)
    formatted_prompt = prompt.format(**filtered_data)
    print("Formatted Prompt:")
    print(formatted_prompt)
    ```

5. **Output**: The output will be a fully formatted prompt that integrates the provided user input and business documentation:

    ```
    Business documentation is crucial for understanding the context of operations. 
    Please refer to the following business details.
    
    User input allows us to tailor our approach based on specific queries.
    We received the following input from the user.

    Ensure the answer follows a professional tone.
    ```

## Error Handling

If a placeholder is missing from the context data, the library will gracefully skip the corresponding piece without breaking the overall template. You can also customize error handling behavior as needed to ensure a seamless user experience.

## Key Advantages

- **YAML-Based Configuration**: Manage prompt templates in a centralized, human-readable format.
- **Dynamic Stacking**: Flexibly assemble prompt pieces to adapt to various scenarios.
- **Integration with LangChain**: Use this library as a lightweight layer for assembling prompts before leveraging LangChain's formatting capabilities.

---

