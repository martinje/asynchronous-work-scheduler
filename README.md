# Asynchronous Work Scheduler

This Python Flask application serves as an asynchronous work scheduler, allowing users to submit work requests, check the status of their requests, and retrieve results when the work is completed.

## Introduction

This example code represents a simple asynchronous work scheduler implemented using Python Flask. The main purpose of the code is to allow users to submit work requests, check the status of their requests, and retrieve results when the work is completed.

Here's a breakdown of what the code does:

1. Work Submission: Users can submit work requests to the scheduler by sending a POST request to the /api endpoint. Each work request is assigned a unique ID, and the server responds with the ID and a URL where users can check the status of their request.
2. Asynchronous Processing: When a work request is submitted, the scheduler starts processing the request in a separate thread. This allows the server to continue handling other requests while the work is being performed asynchronously.
3. Status Checking: Users can check the status of their work requests by sending a GET request to the /api endpoint with the ID of their request. The server responds with the current status of the request, indicating whether the work is still in progress or has been completed.
4. Logging: The code logs the progress of each work request to a file named log.txt, including the start and end times of the work.

Overall, this example code demonstrates how to build a basic asynchronous work scheduler using Flask, enabling efficient handling of work requests while providing users with visibility into the status of their requests.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd asynchronous-work-scheduler
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Starting the Application

To start the Flask application, run the following command:

```bash
python app.py
```

By default, the application will run on `http://localhost:5000/`.

### API Endpoints

#### 1. `POST /api`

Submit a new work request to the scheduler.

**Request Body:**

None

**Response:**

- Status: 202 Accepted
- Body:
    ```json
    {
        "id": "<generated_id>",
        "status_url": "http://localhost:5000/api?id=<generated_id>"
    }
    ```

#### 2. `GET /api`

Check the status of a work request.

**Request Parameters:**

- `id`: The ID of the work request.

**Response:**

- Status: 200 OK (if job is done)
- Body:
    ```json
    {
        "message": "Job is done!"
    }
    ```

- Status: 202 Accepted (if job is still in progress)
- Body:
    ```json
    {
        "message": "Job is still in progress!",
        "estimated_time_completion": "<estimated_completion_time>",
        "seconds_to_completion": "<seconds_to_completion>"
    }
    ```

- Status: 400 Bad Request (if the provided ID is invalid)
- Body:
    ```json
    {
        "message": "Invalid id!"
    }
    ```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
