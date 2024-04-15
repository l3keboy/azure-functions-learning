import azure.functions as func
import logging
from logic import main

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="import_logic_http_trigger")
async def import_logic_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    result = await main.add_1_two_times()

    return func.HttpResponse(
        f"This was a HTTP-triggered Azure function made with python wich does import custom modules (methods) from a file to execute. The result was {result}",
        status_code=200,
    )
