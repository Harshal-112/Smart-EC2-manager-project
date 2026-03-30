# Smart-EC2-manager-project
A simple command-line tool to manage AWS EC2 instances using Python and Boto3.
This tool allows you to list, start, and stop EC2 instances interactively from the terminal.

## 📌 Features

* 🔍 List all **stopped EC2 instances**
* ▶️ Start a selected EC2 instance
* 📡 List all **running EC2 instances** with public IP
* ⏹️ Stop a selected EC2 instance
* ⏳ Uses AWS **waiters** to ensure instance state transitions
* 🛡️ Handles invalid user input (non-numeric / out-of-range)

---

## 🛠️ Tech Stack

* Python 3
* Boto3 (AWS SDK for Python)
* AWS EC2

---

## ⚙️ Prerequisites

Before running this project, make sure you have:

* Python 3 installed
* AWS CLI configured:

* Required IAM permissions:

  * ec2:DescribeInstances
  * ec2:StartInstances
  * ec2:StopInstances


## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Harshal-112/Smart-EC2-manager-project.git
cd Smart-EC2-manager-project
```

2. Install dependencies:

```bash
pip install boto3
```

3. Run the script:

```bash
python script.py
```

---

## 🖥️ Example Usage

```
1. Show stopped instances
2. Start instances
3. Show running instances
4. Stop instance
5. Exit
```

* Select an option
* Choose instance number from list
* Tool performs action and waits for completion

---

## ⚠️ Limitations

* Works only for a single AWS region (hardcoded)
* No tagging filter (acts on all instances)
* No logging system (uses print statements)
* No retry mechanism for failures

---

## 🚀 Future Improvements

* Add filtering using instance tags (e.g., Environment=Dev)
* Convert CLI into argument-based tool (argparse)
* Add logging support
* Support multiple regions
* Improve UI/UX with better formatting

---

## 📚 What I Learned

* Working with AWS EC2 using Boto3
* Handling asynchronous operations using waiters
* Writing modular and structured Python code
* Building interactive CLI tools
* Debugging real-world cloud automation issues

---

## 📄 License

This project is for learning and educational purposes.
