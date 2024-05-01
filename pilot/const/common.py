import os


APP_TYPES = ['Web App', 'Script', 'Mobile App', 'Chrome Extension']
ROLES = {
    'product_owner': ['project_description', 'user_stories', 'user_tasks'],
    'architect': ['architecture'],
    'tech_lead': ['development_planning'],
    'full_stack_developer': ['coding'],
    'dev_ops': ['environment_setup'],
    'code_monkey': ['coding']
}
STEPS = [
    'project_description',
    'user_stories',
    'user_tasks',
    'architecture',
    'environment_setup',
    'development_planning',
    'coding',
    'finished'
]

DEFAULT_IGNORE_PATHS = [
    '.git',
    '.gpt-pilot',
    '.idea',
    '.vscode',
    '.next',
    '.DS_Store',
    '__pycache__',
    "site-packages",
    'node_modules',
    'package-lock.json',
    'venv',
    'dist',
    'build',
    'target',
    "*.min.js",
    "*.min.css",
    "*.svg",
    "*.csv",
    "*.log",
    "go.sum",
]
IGNORE_PATHS = DEFAULT_IGNORE_PATHS + [
    folder for folder
    in os.environ.get('IGNORE_PATHS', '').split(',')
    if folder
]
IGNORE_SIZE_THRESHOLD = 50000  # 50K+ files are ignored by default
PROMPT_DATA_TO_IGNORE = {'directory_tree', 'name'}


EXAMPLE_PROJECT_DESCRIPTION = """
The application is a simple ToDo app built using React. Its primary function is to allow users to manage a list of tasks (todos). Each task has a description and a state (open or completed, with the default state being open). The application is frontend-only, with no user sign-up or authentication process. The goal is to provide a straightforward and user-friendly interface for task management.

Features:
1. Display of Todos: A list that displays all todo items. Each item shows its description and a checkbox to indicate its state (open or completed).
2. Add New Todo: A button to add a new todo item. Clicking this button will prompt the user to enter a description for the new todo.
3. Toggle State: Each todo item includes a checkbox. Checking/unchecking this box toggles the todo's state between open and completed.
4. Local Storage: The application will use the browser's local storage to persist todos between sessions, ensuring that users do not lose their data upon reloading the application.

Functional Specification:
- Upon loading the application, it fetches existing todos from the local storage and displays them in a list.
- Each todo item in the list displays a checkbox and a description. The checkbox reflects the todo's current state (checked for completed, unchecked for open).
- When the user checks or unchecks a checkbox, the application updates the state of the corresponding todo item and saves the updated list to local storage.
- Clicking the "Add New Todo" button prompts the user to enter a description for the new todo. Upon confirmation, the application adds the new todo (with the default state of open) to the list and updates local storage.
- The application does not support deleting or editing todo items to keep the interface and interactions simple.
- Todos persist between sessions using the browser's local storage. The application saves any changes to the todo list (additions or state changes) in local storage and retrieves this data when the application is reloaded.

Technical Specification:
- Platform/Technologies: The application is a web application developed using React. No backend technologies are required.
- Styling: Use Bootstrap 5 for a simple and functional interface. Load Boostrap from the CDN (don't install it locally):
    - https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css
    - https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js
- State Management: Directly in the React component
    - make sure to initialize the state from the local storage as default (... = useState(JSON.parse(localStorage.getItem('todos')) || []) to avoid race conditions
- Data Persistence: The application uses the browser's local storage to persist todos between sessions. It stores the array of todos as a JSON string and parses this data on application load.
"""

EXAMPLE_PROJECT_ARCHITECTURE = {
    "architecture": (
        "The application is a client-side React web application that uses local storage for data persistence. "
        "It consists of a single page with components for listing todos, adding new todos, and toggling their completion status. "
        "State management is handled directly within React components, leveraging useState and useEffect hooks for state manipulation and side effects, respectively. "
        "Bootstrap 5 is used for styling to provide a responsive and accessible UI."
    ),
    "system_dependencies": [
        {
            "name": "Node.js",
            "description": "JavaScript runtime needed to run the React development tools and build the project.",
            "test": "node --version",
            "required_locally": True
        }
    ],
    "package_dependencies": [
        {
            "name": "react",
            "description": "A JavaScript library for building user interfaces."
        },
        {
            "name": "react-dom",
            "description": "Serves as the entry point to the DOM and server renderers for React."
        },
        {
            "name": "bootstrap",
            "description": "Frontend framework for developing responsive and mobile-first websites."
        }
    ],
    "template": "javascript_react"
}

EXAMPLE_PROJECT_PLAN = [
    {
        "description": (
            "Create a new component TodoList: This component will display the list of todo items. "
            "Use localStorage directly to access the current state of todos and map over them, rendering each todo item as a list item. "
            "Each item should display the todo's description and a checkbox that reflects the todo's state (checked for completed, unchecked for open). "
            "When the checkbox is clicked, dispatch an action to toggle the state of the todo. "
            "Also create AddTodo: This component will include a button that, when clicked, displays a prompt asking the user for a description of the new todo. "
            "Upon confirmation, dispatch an action to add the new todo to the state with a default state of open. "
            "Ensure the component also updates the local storage with the new list of todos. "
            "Finally, use TodoList and AddTodo components in App component to implement the required functionality. "
            "Integrate Boostrap 5 for styling - add CSS/JS to index.html, style App.jsx and other files as appropriate."
        )
    }
]

EXAMPLE_PROJECT_DESCRIPTION_CN = """
该应用程序是一个使用React构建的简单ToDo应用程序。它的主要功能是允许用户管理任务列表（todo）。每个任务都有一个描述和状态（打开或完成，默认状态为打开）。该应用程序仅为前端应用程序，没有用户注册或身份验证过程。目标是为任务管理提供一个简单易用的界面。
特征：
1.待办事项显示：显示所有待办事项的列表。每个项目都显示其描述和一个复选框，以指示其状态（打开或完成）。
2.添加新待办事项：用于添加新待办项目的按钮。单击此按钮将提示用户输入新待办事项的描述。
3.切换状态：每个待办事项都包括一个复选框。选中/取消选中此框可在打开和完成之间切换待办事项的状态。
4.本地存储：应用程序将使用浏览器的本地存储在会话之间保持todo，确保用户在重新加载应用程序时不会丢失数据。

功能规范：
-加载应用程序后，它会从本地存储中获取现有的todo，并将它们显示在列表中。
-列表中的每个待办事项都会显示一个复选框和一个说明。复选框反映待办事项的当前状态（选中表示已完成，未选中表示已打开）。
-当用户选中或取消选中复选框时，应用程序会更新相应待办事项的状态，并将更新后的列表保存到本地存储中。
-单击“添加新待办事项”按钮，提示用户输入新待办事项的说明。确认后，应用程序将新的todo（默认状态为打开）添加到列表中，并更新本地存储。
-该应用程序不支持删除或编辑todo项以保持界面和交互的简单性。
-Todos使用浏览器的本地存储在会话之间持久存在。应用程序将对待办事项列表的任何更改（添加或状态更改）保存在本地存储中，并在重新加载应用程序时检索这些数据。

技术规范：
-平台/技术：该应用程序是使用React开发的web应用程序。不需要后端技术。
-风格：使用Bootstrap 5获得简单实用的界面。从CDN加载Boostrap（不要在本地安装）：
- https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css
- https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js
-状态管理：直接在React组件中
-请确保将本地存储中的状态初始化为默认状态（…=useState（JSON.parse（localStorage.getItem（'todos'））||[]），以避免出现竞争条件
-数据持久化：应用程序使用浏览器的本地存储在会话之间持久化todo。它将todo数组存储为JSON字符串，并在应用程序加载时解析这些数据。
"""

EXAMPLE_PROJECT_ARCHITECTURE_CN = {
    "architecture": (
        "该应用程序是一个客户端React web应用程序，使用本地存储实现数据持久性。"
        "它由一个单独的页面组成，其中包含用于列出待办事项、添加新待办事项和切换其完成状态的组件。 "
        "状态管理直接在React组件中处理, 分别利用 useState 和 useEffect 挂钩进行状态操纵和副作用。 "
        "Bootstrap 5用于造型，以提供响应性强且可访问的UI。"
    ),
    "system_dependencies": [
        {
            "name": "Node.js",
            "description": "运行React开发工具和构建项目所需的JavaScript运行时。",
            "test": "node --version",
            "required_locally": True
        }
    ],
    "package_dependencies": [
        {
            "name": "react",
            "description": "一个用于构建用户界面的JavaScript库。"
        },
        {
            "name": "react-dom",
            "description": "充当React的DOM和服务器渲染器的入口点。"
        },
        {
            "name": "bootstrap",
            "description": "用于开发响应式和移动优先网站的前端框架。"
        }
    ],
    "template": "javascript_react"
}

EXAMPLE_PROJECT_PLAN_CN = [
    {
        "description": (
            "创建一个新组件待办事项列表：该组件将显示待办事项的列表。"
            "直接使用localStorage访问todo的当前状态并映射到它们上，将每个todo项呈现为列表项。"
            "每个项目都应该显示待办事项的描述和反映待办事项状态的复选框（选中表示已完成，未选中表示已打开）。"
            "单击复选框后，分派一个操作来切换待办事项的状态。"
            "还要创建AddTodo：这个组件将包括一个按钮，当单击该按钮时，会显示一个提示，要求用户提供新todo的描述。"
            "确认后，分派一个操作，将新的todo添加到默认状态为open的状态。"
            "确保该组件还使用新的待办事项列表更新本地存储。"
            "最后，使用应用程序组件中的TodoList和AddTodo组件来实现所需的功能。"
            "Integrate Boostrap 5 for styling - add CSS/JS to index.html, style App.jsx and other files as appropriate."
            "集成 Boostrap 5 进行样式设置-将CSS/JS添加到index.html、样式App.jsx和其他相关的文件中。"
        )
    }
]
