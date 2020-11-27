using System.Linq;

namespace BrainTrain.Exercise1
{
    public class Exercise1
    {
        public int solution(int[] A)
        {
            var input = A.ToList();

            input.Sort();

            var min = 0;
            foreach (var number in input)
            {
                if (number > min +1)
                {
                    break;
                }

                if (number > min)
                {
                    min = number;
                }
            }
            return min+1;
        }
    }
}
