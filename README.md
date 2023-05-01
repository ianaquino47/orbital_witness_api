
Getting Started
---------------

To get started with this API, follow these steps:

1.  Clone the repository to your local machine.
2.  Create a virtual environment using your preferred method and activate it.
3.  Install the dependencies by running `pip install -r requirements.txt`.
4.  Start the server by running `uvicorn main:app --reload`.

Front End
-------------
I created a simple frontend for testing the API.

1.  While your uvicorn server is running, open a new terminal window and navigate into the `frontend` folder on your terminal.
2.  Run `npm install` to install project dependencies
3.  Run `npm start` to start the development server.
4.  Open your web browser and navigate to the url address with the correct port number
   based on what it says on your terminal (most likely `localhost:3000` ).
It should look like below.
![alt text](/frontend.png)

API Endpoints
-------------

This API provides the following endpoints:

### GET /api/titles

Returns a list of all titles, filtered and sorted based on query parameters.

Query Parameters:
-   `title_class`: Filter titles by `title_class` (e.g. "Freehold", "Leasehold")
-   `_sort`: Sort titles by `id` or `title_number`
-   `_order`: Sort order, either `asc` (ascending) or `desc` (descending)

### GET /api/titles/{id}

Returns information about a single title, specified by its ID.

Running tests
-----------------
Within the main directory and virtual environment, run the tests with
```pytest``` command.

Technologies Used
-----------------

This API is built using the following technologies:

-   FastAPI
-   uvicorn

Contributing
------------

Contributions to this project are welcome. To get started, fork the repository and submit a pull request.

License
-------

This project is licensed under the MIT License. See the [LICENSE](https://chat.openai.com/LICENSE) file for details.