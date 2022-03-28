const a = () => {
  console.log("a 시작");
  setTimeout(b, 0)
//   b();
  console.log("a 끝");
};

const b = async () => {
  console.log("b 시작");
  await c(); // 일시정지
  console.log("b 끝");
};

const c = async () => {
  console.log("c 시작");
  await d(); 
  console.log("c 끝");
};

const d = () => {
  console.log("d")
};

a();