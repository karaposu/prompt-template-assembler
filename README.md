
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


