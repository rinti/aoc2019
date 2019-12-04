range = 357253..892942

defmodule Advent do
  def test(x) do
    charlist = Integer.to_charlist(x)
    sorted_charlist = Enum.sort(charlist)
    str = to_string sorted_charlist

    is_increasing = charlist == sorted_charlist
    has_double = Enum.any?(
      ["11", "22", "33", "44", "55", "66", "77", "88", "99", "00"],
      fn x -> str =~ x end
    )

    if is_increasing and has_double do
      true
    end
  end
end

IO.puts Enum.count(Enum.filter(range, fn x -> Advent.test x end))
