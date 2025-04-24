# MCP-AGENT-Example

## Overview

MCP-AGENT-Example is a modern and professional implementation of an agent-based system leveraging the power of the Model Context Protocol (MCP). This project demonstrates how to integrate advanced AI models with external tools to perform complex tasks efficiently. The agent is designed to interact with tools like Playwright to fetch and process information dynamically.

## Features

- **AI-Powered Agent**: Utilizes the `ChatGroq` model for natural language understanding and task execution.
- **Tool Integration**: Seamlessly integrates with external tools like Playwright via MCP.
- **Asynchronous Execution**: Built with Python's asyncio for high-performance asynchronous operations.
- **Customizable**: Easily extendable to include additional tools and configurations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/MCP-AGENT-Example.git
   cd MCP-AGENT-Example
   ```
2. Install dependencies:

   ```bash
   uv sync
   ```
3. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Add your `GROQ_API_KEY`:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

Run the main script to execute the agent:

```bash
python agent/main.py
```

The agent will use the tools to fetch and process information. For example, it can fetch the weather in Tunis using the integrated tools.

## Project Structure

```
MCP-AGENT-Example
│
├── agent/
│   ├── main.py          # Main script to run the agent
│   ├── pyproject.toml   # Project configuration
│   ├── README.md        # Project documentation
│   └── uv.lock          # Dependency lock file
│
├── LICENSE              # License file
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:

- **Email**: amenallah8bouhachem@gmail.com
- **GitHub**: [Amenallah Bouhachem](https://github.com/AmenallahBouhachem)

---

Thank you for using MCP-AGENT-Example! 🚀
