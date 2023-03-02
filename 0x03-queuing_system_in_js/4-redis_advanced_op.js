import { createClient, print } from "redis";
const client = createClient();
import { promisify } from "util";
const hgetall = promisify(client.hgetall).bind(client);

async function hashValue() {
  const values = {
    Portland: 50,
    Seattle: 80,
    "New York": 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const item in values) {
    client.hset("HolbertonSchools", item, values[item], print);
  }

  const result = await hgetall("HolbertonSchools");
  consoole.log(result);
}

hashValue();
