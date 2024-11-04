# Autonomous-Agentic-Tools
Its an dynamic platform enabling Large Language Models (LLMs) to autonomously create, share, and use tools. PoT fosters a collaborative environment where AI agents can expand their capabilities, automate tasks, and adapt to diverse needs, making it a versatile solution for tool-driven intelligence and innovation across applications.

### Key Features:
- **Automated Tool Creation:** When given a task by a human user, an agent will first search the "pot" for an existing tool that can complete the task. If no suitable tool is found, the agent will autonomously create a new tool tailored to the task at hand.
- **Collaborative Environment:** Tools created by one agent are made accessible to other agents, fostering a collaborative ecosystem where agents can learn from and build upon each other's work.
- **Efficient Task Resolution:** By leveraging existing tools in the pot, agents can quickly and efficiently solve user problems, reducing redundancy and maximizing resource utilization.

![Workflow of the Autonomous Agentic Tools](images/Diagram.jpg)

## How It Works
1. **User Input:** A human user provides input to an LLM agent, specifying a task or problem that needs to be solved.
2. **Tool Search:** The agent checks the PoT to see if there is an existing tool that can be used to complete the task.
3. **Tool Utilization:** If a relevant tool is found, the agent utilizes it to complete the task.
4. **Tool Creation:** If no suitable tool exists, the agent autonomously creates a new tool, stores it in the PoT, and then uses it to complete the task.
5. **Tool Sharing:** The newly created tool becomes available in the PoT for other agents to use in future tasks.

## Why PoT?
PoT is designed to enhance the efficiency and autonomy of LLM agents by providing a shared platform for tool creation and utilization. This reduces the need for agents to repeatedly solve the same problems and allows them to focus on creating more sophisticated and innovative solutions.

## Getting Started
To get started with PoT:
1. Clone the repository: `https://github.com/Darshilgajera1/Autonomous-Agentic-Tools.git`
2. Navigate to the project directory: `cd pot`
3. Install the necessary dependencies: `pip install -r requirements.txt`
4. It requires an OpenAI API keys So configure first.
5. To run project: `python3 test.py`
 
## Contributing
Contributions are welcome! Whether it's adding new features, fixing bugs, or improving documentation, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or suggestions, please feel free to contact me at my telegram [@darshilgajera].

---

Thank you for checking out Autonomous Agentic Tools System! We hope it becomes an invaluable platform in your AI development journey.
