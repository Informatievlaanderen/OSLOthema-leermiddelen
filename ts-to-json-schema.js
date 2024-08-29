const tsj = require("ts-json-schema-generator");
const fs = require("fs");
const path = require("path");

/** @type {import('ts-json-schema-generator/dist/src/Config').Config} */
const config = {
  path: path.join(__dirname, "/types/configuration.ts"),
  tsconfig: path.join(__dirname, "tsconfig.json"),
  type: "Configuration", // Or <type-name> if you want to generate schema for that one type only
};

const output_path = path.join(__dirname, "/schemas/configuration.json");

const schema = tsj.createGenerator(config).createSchema(config.type);
const schemaString = JSON.stringify(schema, null, 2);
fs.writeFile(output_path, schemaString, (err) => {
  if (err) throw err;
});
