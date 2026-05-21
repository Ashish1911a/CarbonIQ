import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function YoYChart({ data }) {

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
        Year-over-Year Emissions
      </h2>

      <div className="w-full h-[380px]">

        <ResponsiveContainer width="100%" height="100%">

          <BarChart
            data={data}
            margin={{
              top: 20,
              right: 30,
              left: 20,
              bottom: 20,
            }}
          >

            <XAxis dataKey="year" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar
              dataKey="scope1"
              stackId="a"
              fill="#16a34a"
              name="Scope 1"
            />

            <Bar
              dataKey="scope2"
              stackId="a"
              fill="#2563eb"
              name="Scope 2"
            />

            <Bar
              dataKey="scope3"
              stackId="a"
              fill="#ea580c"
              name="Scope 3"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}