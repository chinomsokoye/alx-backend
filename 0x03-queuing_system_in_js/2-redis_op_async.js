import { createClient, print } from "redis";
const client = createClient();
import { promisify } from "util";
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
  console.log(`Redis client connected to the server`);
});

client.on("error", (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
  client.get(schoolName, print);
}

function displaySchoolValue(schoolName) {
  const result = await gettAsync(schoolName);
  console.log(result);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
