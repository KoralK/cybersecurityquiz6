import streamlit as st

def main():
    st.title("Privilege Escalation & Exploitation Quiz")
    st.markdown("Test your knowledge of vulnerability exploitation and privilege escalation tactics.")

    questions = [
        {
            "question": "What is the primary purpose of a 'zero-day exploit'?",
            "options": [
                "To patch newly discovered vulnerabilities",
                "To exploit vulnerabilities before a fix is available",
                "To escalate privileges on patched systems"
            ],
            "answer": "To exploit vulnerabilities before a fix is available",
            "explanation": "Zero-day exploits target unpatched vulnerabilities for unauthorized access."
        },
        {
            "question": "What distinguishes horizontal privilege escalation from vertical privilege escalation?",
            "options": [
                "Horizontal: Gaining admin rights; Vertical: Accessing another user’s account",
                "Horizontal: Accessing accounts with the same privileges; Vertical: Gaining higher privileges",
                "Horizontal: Exploiting DLLs; Vertical: Creating backdoors"
            ],
            "answer": "Horizontal: Accessing accounts with the same privileges; Vertical: Gaining higher privileges",
            "explanation": "Horizontal = same-level access; Vertical = higher privileges (e.g., user → admin)."
        },
        {
            "question": "How does DLL hijacking work?",
            "options": [
                "Encrypting legitimate DLLs to block execution",
                "Replacing legitimate DLLs with malicious ones in application directories",
                "Deleting DLLs to crash the system"
            ],
            "answer": "Replacing legitimate DLLs with malicious ones in application directories",
            "explanation": "Attackers replace legitimate Dynamic Link Libraries (DLLs) with malicious versions, which are loaded by applications to execute unauthorized code."
        },
        {
            "question": "Which tool is mentioned for exploiting DLL vulnerabilities?",
            "options": [
                "Wireshark",
                "Metasploit",
                "Nmap"
            ],
            "answer": "Metasploit",
            "explanation": "Metasploit includes modules for DLL hijacking, enabling attackers to escalate privileges or maintain access."
        },
        {
            "question": "What is a common method for maintaining access after exploitation?",
            "options": [
                "Encrypting user data",
                "Creating a backdoor",
                "Disabling firewalls"
            ],
            "answer": "Creating a backdoor",
            "explanation": "Backdoors allow attackers to re-enter compromised systems without re-exploiting vulnerabilities, even after patches are applied."
         },
        {
            "question": "How might an attacker reset passwords after gaining admin privileges?",
            "options": [
                "Using net user commands in Command Prompt",
                "Deleting user accounts",
                 "Sending phishing emails"
            ],
            "answer": "Using net user commands in Command Prompt",
            "explanation": "The net user command in Windows allows admins to reset passwords for any account, a tactic attackers use post-escalation."
         },
        {
            "question": "Which countermeasure BEST mitigates privilege escalation?",
            "options": [
                "Enabling default passwords",
                 "Implementing the principle of least privilege",
                "Disabling antivirus software"
             ],
             "answer": "Implementing the principle of least privilege",
             "explanation": "Restricting users and applications to the minimum necessary privileges limits the damage from compromised accounts."
        },
        {
            "question": "What is a key defense against DLL hijacking?",
            "options": [
                "Allowing applications to run with admin rights",
                "Regularly patching software",
                 "Storing DLLs in public directories"
            ],
             "answer": "Regularly patching software",
             "explanation": "Patching fixes vulnerabilities that attackers exploit to replace legitimate DLLs with malicious ones."
        }
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        selected = st.radio("Choose an answer:", q["options"], key=f"q{i}", index=None)
        
        if st.button("Check Answer", key=f"btn{i}"):
            if selected == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")
            with st.expander("Explanation"):
                st.write(q["explanation"])
            st.write("---")

    st.header("Results")
    st.write(f"Final Score: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()