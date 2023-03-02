const kue = require("kue");
const queue = kue.createQueue();

const JobData = {
  phoneNumber: "08023585254",
  message: "Code for account verification",
};

const job = queue.create("push_notification_code", JobData).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});

job.on("progress", () => {
  console.log("Notification job failed");
});
