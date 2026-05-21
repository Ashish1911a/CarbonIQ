import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

export default function TrendChart({ data }) {

  return (

    <div className="
      bg-white
      rounded-2xl
      shadow-lg
      p-6
      w-full
      h-[500px]
    ">

      <h2 className="text-2xl font-bold mb-6 text-gray-800">
        Monthly Emission Trends
      </h2>

      <div className="w-full h-[380px]">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart
            data={data}
            margin={{
              top: 20,
              right: 30,
              left: 20,
              bottom: 20,
            }}
          >

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="emissions"
              stroke="#16a34a"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}