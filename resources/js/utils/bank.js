import bankJson from '../banks.json';

export const banks = () => {
  return Object.values(bankJson);
};
