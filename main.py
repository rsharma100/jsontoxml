from fastapi import FastAPI, File, UploadFile, Response
import json
import dicttoxml
import uvicorn

app = FastAPI()

@app.post("/convert-json-to-xml/")
async def convert_json_to_xml(file: UploadFile = File(...)):
    contents = await file.read()
    json_data = json.loads(contents)
    xml_data = dicttoxml.dicttoxml(json_data)
    return Response(content=xml_data, media_type="application/xml")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)
