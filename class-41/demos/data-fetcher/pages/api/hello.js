export default function handler(req, res) {
  const name = req.query['name'];
  console.log(req);
  res.status(200).json({ name })
}