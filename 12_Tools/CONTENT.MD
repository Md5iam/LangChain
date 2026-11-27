03:05 - What is a tool?
11:53 - Built-in Tools
20:56 - Custom Tools
31:05 - Create Custom Tools
41:03 - Toolkits


Custom Tool (@tool): Used to convert a normal Python function into a LangChain tool. We can customize its name, description, input parameters, type hints, and tool logic. It is suitable for simple tools where we don't need to directly override the internal methods of the tool class.

Structured Tool: Similar to a custom tool, but provides more control over the input structure using schemas like Pydantic. We can define field descriptions, validation rules, constraints, optional fields, and complex input structures. However, it doesn't give us direct class inheritance and method-overriding control like BaseTool.

BaseTool: Used to create tools by inheriting from LangChain's base tool class. It gives us more direct control over the tool's configuration and execution behavior. We can override methods like _run() and _arun(), maintain internal state, add helper methods, and customize how the tool executes instead of relying mainly on the default function wrapper.