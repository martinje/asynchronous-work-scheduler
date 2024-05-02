# Asynchronous Work Scheduler

This Python Flask application serves as an asynchronous work scheduler, allowing users to submit work requests, check the status of their requests, and retrieve results when the work is completed.

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
