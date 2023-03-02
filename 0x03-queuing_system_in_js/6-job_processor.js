const kue = require("kue");
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
}

queue.create("push_notification_code", (job, done) => {
  const {phoneNumber, message} = job.data;
  sendNotification(phoneNumber, message);
  done();
});
