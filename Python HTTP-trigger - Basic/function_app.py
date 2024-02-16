import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="basic_http_trigger")
def basic_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger - Basic functions starting.")

    return func.HttpResponse(
        "This is the Python HTTP trigger - basic. A request is done, the function runs, does some task if needed, and gives a response"
    )
