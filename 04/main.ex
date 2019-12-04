range = 357253..892942

defmodule Advent do
  def test(x) do
    charlist = Integer.to_charlist(x)
    sorted_charlist = Enum.sort(charlist)
    str = to_string sorted_charlist

    is_increasing = charlist == sorted_charlist

    char_count = str |> String.graphemes() |> Enum.reduce(%{}, fn char, acc ->
      Map.put(acc, char, (acc[char] || 0) + 1)
    end)

    elegible_counts = Enum.filter(
        Map.values(char_count), fn c -> c < 2 || c > 1 && rem(c, 2) == 0 end
    )
    has_double_part2 = Enum.any?(elegible_counts, fn x -> x == 2 end)

    # has_double_part1 = Enum.any?(
    #   ["11", "22", "33", "44", "55", "66", "77", "88", "99", "00"],
    #   fn x -> str =~ x end
    # )

    if is_increasing and has_double_part2 do
      true
    end
  end
end

IO.puts Enum.count(Enum.filter(range, fn x -> Advent.test x end))
