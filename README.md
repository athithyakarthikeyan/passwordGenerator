# Python Password Generator

A user-friendly Python application to generate secure and random passwords. The application uses Tkinter for the GUI and allows users to customize the length and complexity of the passwords. Additionally, it provides features to save generated passwords with optional labels.

## Features

- **Customizable Password Length**: Users can specify the desired length of the password.
- **Character Types**: Includes uppercase letters, lowercase letters, digits, and special characters in the generated passwords.
- **Graphical User Interface (GUI)**: Built using Tkinter for ease of use.
- **Save Passwords**: Option to save generated passwords to a file with optional labels.
- **Copy to Clipboard**: Generated passwords can be copied directly to the clipboard for easy use.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/passwordGenerator.git
    cd passwordGenerator
    ```

2. **Run the Application**:
    ```bash
    python sourcecode.py
    ```

## Usage

1. Enter the desired password length.
2. Click the "Generate Password" button to create a new password.
3. The generated password will be displayed in the GUI.
4. Optionally, enter a label for the password.
5. Click the "Save Password" button to save the password to a file.

## Code Overview

- **Password Generation**: Generates passwords using a combination of letters, digits, and special characters.
- **GUI**: Utilizes Tkinter to create an intuitive interface for user interaction.
- **File Saving**: Saves the generated password to a specified file path with an optional label.

## File Structure

```plaintext
password-generator/
├── sourcecode.py
├── README.md
