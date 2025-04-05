import { useHttp } from "../config";

type TestScenarioSchema = {
  websiteUrl: string;
  testObjective: string;
  description: string;
  precondition: string;
  captureScreenshots: boolean;
};
type CreateTestScenarioDTO = TestScenarioSchema;

export const getTestScenario = () => {
  const http = useHttp<CreateTestScenarioDTO>();
  return http.request("get", "/api/scenario");
};
