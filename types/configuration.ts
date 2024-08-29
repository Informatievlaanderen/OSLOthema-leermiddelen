export interface Configuration {
  title: string;
  category: string;
  usage: string;
  status: string;
  responsibleOrganisation: {
    name: string;
    uri: string;
  };
  publicationDate: string;
  descriptionFileName: string;
  specificationDocuments: Document[];
  documentation: Document[];
  charter: Document;
  reports: Document[];
  presentations: Document[];
  dateOfRegistration: string;
  dateOfAcknowledgementByWorkingGroup: string;
  dateOfAcknowledgementBySteeringCommittee: string;
  datePublicReviewStart: string;
  datePublicReviewEnd: string;
  endOfPublicationDate: string;
}

interface Document {
  name?: string;
  resourceReference?: string;
}
