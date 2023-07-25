const express = require("express");
const { exec } = require("child_process");
const app = express();

app.use(express.static("public"));

app.get("/runform", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});
app.get("/run", (req, res) => {
  //res.sendFile(__dirname + "/livecmd.html")
  const cname = req.query.cname;
  const cimage = req.query.cimage;

  exec(
    "docker run -dit --name " + cname + " " + cimage,
    (err, stdout, stderr) => {
      res.send(stdout);
    }
  );
});
app.get("/cmd", (req, res) => {
  res.sendFile(__dirname + "/livecmd.html");
});
app.get("/comman", (req, res) => {
  const cmd = req.query.cmd;
  exec(cmd, (err, stdout, stderr) => {
    res.send(stdout);
  });
});

app.get("/ps", (req, res) => {
  exec("docker ps | tail -n +2 ", (err, stdout, stderr) => {
    res.send(stdout);
  });
});

app.get("/del", (req, res) => {
  const del = req.query.cdname;
  exec("docker stop " + del, (err, stdout, stderr) => {
    res.send(stdout);
  });
});
app.get("/deleteall", (req, res) => {
  exec("docker rm -f $(docker ps -a -q)", (err, stdout, stderr) => {
    res.send(stdout);
  });
});
app.get("/cpullos", (req, res) => {
  const cpullos = req.query.cpullos;
  exec("docker pull " + cpullos, (err, stdout, stderr) => {
    res.send(stdout);
  });
});
app.get("/allpulledimages", (req, res) => {
  exec("docker images", (err, stdout, stderr) => {
    console.log(stdout);
    res.send(stdout);
  });
});

app.get("/cidelete", (req, res) => {
  const cidelete = req.query.cidelete;
  exec("docker rmi -f " + cidelete, (err, stdout, stderr) => {
    res.send(stdout);
  });
});
app.listen(3000, () => {
  console.log("DockEase started at port 3000");
});
