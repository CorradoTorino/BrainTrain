using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BrainTrain.Exercise1
{
    [TestClass]
    public class Exercise1Tests
    {
        [TestMethod]
        public void TestExample()
        {
            var sut = new Exercise1();
            var input = new[] { 1, 3, 6, 4, 1, 2 };

            var result = sut.solution(input);

            Assert.AreEqual(5, result);
        }
    }
}