import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KitStatusComponent } from './kit-status.component';

describe('KitStatusComponent', () => {
  let component: KitStatusComponent;
  let fixture: ComponentFixture<KitStatusComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [KitStatusComponent]
    });
    fixture = TestBed.createComponent(KitStatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
