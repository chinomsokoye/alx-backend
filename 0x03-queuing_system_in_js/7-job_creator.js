const kue = require("kue");
const queue = kue.createQueue();

const Jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518783",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518782",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518782",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518782",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code to verify your account",
  },
  {
    phoneNumber: "4153518782",
    message: "This is the code to verify your account",
  },
];
  
const queue = kue.createQueue();

jobs.forEach((job) => {
  const jobObject = queue
    .create("push_notification_code_2", job)
    .save((error) => {
      if (!error) console.log(`Notification job created: ${jobObject.id}`);
    });

  jobObject.on("complete", () => {
    console.log(`Notification job completed ${jobObject.id}`);
  });

  jobObject.on("failed", (error) => {
    console.log(`Notification job ${jobObject.id} failed: ${error}`);
  });

  jobObject.on("progress", (progress) => {
    console.log(`Notification job ${jobObject.id} ${progress}% completed`);
  });
});
