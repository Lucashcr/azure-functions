from azure.functions import FunctionApp, HttpRequest


app = FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="req")
def main(req: HttpRequest) -> str:
    user = req.params.get("user")
    return f"Hello, {user}!"
