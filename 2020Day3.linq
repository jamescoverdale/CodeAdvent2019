void Main()
{
	var lines = input.Split('\r');	
	var rowlength = lines[0].Trim().Length;
	string[,] map = new string[rowlength, lines.Length];		
	
	for(int i = 0; i < rowlength; i++)
	{
		for(int j =0; j < lines.Length; j++)
			map[i, j] = lines[j].Trim().ToCharArray()[i].ToString();
	}	
	
	var part1Calc = CalculateTrees(3,1).Dump();
	
	var part2Calc = (CalculateTrees(1,1) *
					 CalculateTrees(3,1) *
					 CalculateTrees(5,1) *
					 CalculateTrees(7,1) *
					 CalculateTrees(1,2)).Dump();

	double CalculateTrees(int right, int down)
	{
		int currentColPos = 0;
		int currentLinePos = 0;
		int count = 0;

		while (currentLinePos < lines.Length - 1)
		{
			currentColPos += right;

			if (currentColPos >= rowlength)
				currentColPos = currentColPos % rowlength;

			currentLinePos += down;		

			string loc = map[currentColPos, currentLinePos];

			if (loc == "#")
				count++;
		}
		
		return count;
	}

}

string input = @"..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#";
