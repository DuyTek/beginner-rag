import { RouteObject } from "react-router";
import { TestScenarioCreationPage } from "../page";
import { Result } from "../page/Result";

export const routes: RouteObject[] = [
  {
    index: true,
    path: "/",
    Component: TestScenarioCreationPage,
  },
  {
    path: "/result",
    Component: Result,
  },
];
